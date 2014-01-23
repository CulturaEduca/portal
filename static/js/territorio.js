function init() {

	var map = new OpenLayers.Map('mapa', {});
	var from_proj = new OpenLayers.Projection("EPSG:4326");
	var to_proj = new OpenLayers.Projection("EPSG:900913");
	var zoom = 16;
	var size = new OpenLayers.Size(21, 25);
	var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h);

	var latitude_centro = document.getElementById('latitude_centro').innerHTML;
	var longitude_centro = document.getElementById('longitude_centro').innerHTML;
	var codigo_inep = document.getElementById('codigo_inep').innerHTML;
	var codigo_ibge = document.getElementById('codigo_ibge').innerHTML;

	var osm_layer = new OpenLayers.Layer.OSM('Mapa OSM');
	var gmap = new OpenLayers.Layer.Google("Google Maps");
	var mapbox = new OpenLayers.Layer.XYZ(
		"Mapbox",
		[
			"http://a.tiles.mapbox.com/v3/inaebatistoni.map-t89cxkrw/${z}/${x}/${y}.png",
		], {
			attribution: "",
          	sphericalMercator: true,
          	wrapDateLine: true,
          	transitionEffect: "resize",
          	buffer: 1,
          	numZoomLevels: 17
		});

	var contorno = new OpenLayers.Layer.Vector("Contorno do município", {
		strategies: [new OpenLayers.Strategy.Fixed()],
		visibility: false,
		protocol: new OpenLayers.Protocol.HTTP({
			url: "/ibge/contorno_municipio/" + codigo_ibge + "/",
			format: new OpenLayers.Format.GeoJSON()
		})
	});

	// territorio educativo - area e estilos
	var territorio = new OpenLayers.Layer.Vector("Territorio Educativo", {
		strategies: [new OpenLayers.Strategy.Fixed()],
		visibility: true,
		protocol: new OpenLayers.Protocol.HTTP({
			url: "/territorio/geojson/" + codigo_inep + "/",
			format: new OpenLayers.Format.GeoJSON()
		})
	});

	// KML inicio

	var escola = new OpenLayers.Layer.Vector('Escola', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/escola/kml/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});

	// KML fim

	// Saude

	var saude = new OpenLayers.Layer.Vector('Saude', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/saude/escola/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});

	// Museus

	var museus = new OpenLayers.Layer.Vector('Museus', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/museu/escola/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});


	// bibliotecas 

	var bibliotecas = new OpenLayers.Layer.Vector('Bibliotecas', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/biblioteca/escola/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});

	//  cras

	var cras = new OpenLayers.Layer.Vector('CRAS', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/cra/escola/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});

	// Teatro

	var teatro = new OpenLayers.Layer.Vector('Teatro', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/teatro/territorio/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});

	// Cinema

	var cinema = new OpenLayers.Layer.Vector('Cinema', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/cinema/escola/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});

	// CentroCiencia

	var centro_ciencia = new OpenLayers.Layer.Vector('Centro de Ciencia', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/centro_ciencia/escola/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});

	// Salas Verdes

	var sala_verde = new OpenLayers.Layer.Vector('Sala Verde', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/sala_verde/escola/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});

	// Ponto Cultura

	var ponto_cultura = new OpenLayers.Layer.Vector('Pontos de Cultura', {
		projection: map.displayProjection,
		strategies: [new OpenLayers.Strategy.Fixed()],
		protocol: new OpenLayers.Protocol.HTTP({
			url: '/ponto_cultura/escola/' + codigo_inep + '/',
			format: new OpenLayers.Format.KML({
				extractStyles: true,
				extractAttributes: true
			})
		})
	});


	map.addLayers([
		mapbox,
		osm_layer,
		contorno,
		territorio,
		escola,
		saude,
		teatro,
		museus,
        bibliotecas,
        cras,
        cinema,
        centro_ciencia,
        sala_verde,
        ponto_cultura,
	]);


	// POPUP KML inicio

	select = new OpenLayers.Control.SelectFeature([escola, 
		museus, 
		saude, 
		teatro, 
		bibliotecas, 
		cinema,
		centro_ciencia,
		sala_verde,
		ponto_cultura,
		]);
	
	escola.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});

	museus.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});

	saude.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});

	teatro.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});

	bibliotecas.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});

	cinema.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});

	centro_ciencia.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});

	sala_verde.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});

	ponto_cultura.events.on({
		"featureselected": onFeatureSelect,
		"featureunselected": onFeatureUnselect
	});


	map.addControl(select);
	select.activate();

	// POPUP KML fim

	var contorno_estilo = new OpenLayers.Style({
		'fillColor': '#FF9852',
		'fillOpacity': .0,
		'fontColor': '#000000',
		'fontFamily': 'arial, sans-serif',
		'fontSize': '.9em',
		'fontWeight': 'bold',
		'strokeColor': '#000000',
		'strokeWidth': 1,

	});

	var contorno_estilo_mapa = new OpenLayers.StyleMap({
		'default': contorno_estilo
	});

	contorno.styleMap = contorno_estilo_mapa;

	var territorio_estilo = new OpenLayers.Style({
		'fillColor': '#FF9852',
		'fillOpacity': .2,
		'fontColor': '#000000',
		'fontFamily': 'arial, sans-serif',
		'fontSize': '.9em',
		'fontWeight': 'bold',
		// 'label': 'Território Educativo',
		'strokeColor': '#FF9852',
		'strokeWidth': 1,

	});

	var territorio_estilo_mapa = new OpenLayers.StyleMap({
		'default': territorio_estilo
	});

	territorio.styleMap = territorio_estilo_mapa;

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
	    var content = "<a href='" + feature.attributes.description + "/'>" + feature.attributes.name + "</a>"
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
