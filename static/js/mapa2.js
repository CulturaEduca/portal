function init() {

	var map = new OpenLayers.Map('mapa', {});
	var from_proj = new OpenLayers.Projection("EPSG:4326");
	var to_proj = new OpenLayers.Projection("EPSG:900913");
	var zoom = 11;
	var size = new OpenLayers.Size(21, 25);
	var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h);

	var latitude_centro = document.getElementById('latitude_centro').innerHTML;
	var longitude_centro = document.getElementById('longitude_centro').innerHTML;
	var codigo_ibge = document.getElementById('codigo_ibge').innerHTML;

	var osm_layer = new OpenLayers.Layer.OSM('Mapa OSM');
	var gmap = new OpenLayers.Layer.Google("Google Maps");
	var mapbox = new OpenLayers.Layer.XYZ(
		"Mapbox",
		[
			"http://a.tiles.mapbox.com/v3/nodeware.map-c47vwf8j/${z}/${x}/${y}.png",
		], {
			attribution: "",
          	sphericalMercator: true,
          	wrapDateLine: true,
          	transitionEffect: "resize",
          	buffer: 1,
          	numZoomLevels: 17
		});

	var layer1 = new OpenLayers.Layer.Vector("Contorno do município", {
		strategies: [new OpenLayers.Strategy.Fixed()],
		visibility: true,
		protocol: new OpenLayers.Protocol.HTTP({
			url: "/ibge/contorno_municipio/" + codigo_ibge + "/",
			format: new OpenLayers.Format.GeoJSON()
		})
	});


	// KML inicio

	var escola_kml = new OpenLayers.Layer.Vector('Escola KML', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed(),
		new OpenLayers.Strategy.Cluster()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/escola/kml_escolas/' + codigo_ibge + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});

	// KML fim

	// POPUP KML inicio

	select = new OpenLayers.Control.SelectFeature(escola_kml);
	escola_kml.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});

	map.addControl(select);
	select.activate();

	// POPUP KML fim


	var vector_style = new OpenLayers.Style({
		'fillColor': '#669933',
		'fillOpacity': .8,
		'fontColor': '#f0f0f0',
		'fontFamily': 'arial, sans-serif',
		'fontSize': '.9em',
		'fontWeight': 'bold',
		'label': '${num_points}',
		'pointRadius': '${point_radius}',
		'strokeColor': '#aaee77',
		'strokeWidth': 3,
		 
		// 'externalGraphic': '/static/mapa/escola.png'
	},
	{
		context: {
			num_points: function(feature){ 

				return feature.attributes.count; 
			},
			point_radius: function(feature){

				return 9 + (feature.attributes.count)
			}
		}
	});

	var vector_style_map = new OpenLayers.StyleMap({
		'default': vector_style
	});

	escola_kml.styleMap = vector_style_map;

	map.addLayers([
		mapbox,
		osm_layer,
		layer1,
		escola_kml,
		
	]);

	map.addControl(new OpenLayers.Control.LayerSwitcher({}));
	map.setCenter (new OpenLayers.LonLat(longitude_centro, latitude_centro).transform(from_proj, to_proj), zoom);

	if(!map.getCenter()) {
		map.zoomToMaxExtent();
	}

		function onPopupClose(evt) {
		select.unselectAll();
	}

	function onFeatureSelect(event) {
	    var feature = event.feature;
	    var content = "<h2>"+feature.attributes.name + "</h2>" + feature.attributes.description;
	    if (content.search("<script") != -1) {
	        content = "Content contained Javascript! Escaped content below.<br>" + content.replace(/</g, "&lt;");
	}
    popup = new OpenLayers.Popup.FramedCloud("chicken", 
        feature.geometry.getBounds().getCenterLonLat(),
        new OpenLayers.Size(100,100),
        content,
        null, true, onPopupClose);
    feature.popup = popup;
    map.addPopup(popup);
}

function onFeatureUnselect(event) {
    var feature = event.feature;
    if(feature.popup) {
        map.removePopup(feature.popup);
        feature.popup.destroy();
        delete feature.popup;
    }
}

}