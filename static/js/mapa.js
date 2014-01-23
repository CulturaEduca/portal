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

	var escolas = new OpenLayers.Layer.Vector("Escolas", {
		strategies: [new OpenLayers.Strategy.Fixed(),
		new OpenLayers.Strategy.Cluster()
		],
		visibility: true,
		protocol: new OpenLayers.Protocol.HTTP({
			url: "/escola/geojson/" + codigo_ibge + "/",
			format: new OpenLayers.Format.GeoJSON()
		})
	});

	var icone_escola = new OpenLayers.Icon('/static/mapa/escola.png', size, offset);



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

			},
			

		}

	});

	var vector_style_map = new OpenLayers.StyleMap({
		'default': vector_style
	});

	escolas.styleMap = vector_style_map;
	escolas.icon = icone_escola;


	map.addLayers([
		mapbox,
		osm_layer,
		layer1,
		escolas,
		
	]);

	map.addControl(new OpenLayers.Control.LayerSwitcher({}));
	map.setCenter (new OpenLayers.LonLat(longitude_centro, latitude_centro).transform(from_proj, to_proj), zoom);

	if(!map.getCenter()) {
		map.zoomToMaxExtent();
	}
}