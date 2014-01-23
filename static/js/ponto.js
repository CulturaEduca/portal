function init() {

	var map = new OpenLayers.Map('mapa', {});
	var from_proj = new OpenLayers.Projection("EPSG:4326");
	var to_proj = new OpenLayers.Projection("EPSG:900913");
	var zoom = 16;
	var size = new OpenLayers.Size(21, 25);
	var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h);

	var latitude_centro = document.getElementById('latitude_centro').innerHTML;
	var longitude_centro = document.getElementById('longitude_centro').innerHTML;
	var nome_ponto = document.getElementById('nome_ponto').innerHTML;
	var icone = document.getElementById('icone').innerHTML;

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
	map.addLayer(mapbox)
	map.setCenter(new OpenLayers.LonLat(longitude_centro, latitude_centro), 0);

	var markers = new OpenLayers.Layer.Markers(nome_ponto);
	map.addLayer(markers);

	var icon = new OpenLayers.Icon(icone, size, offset);


	markers.addMarker(new OpenLayers.Marker(new OpenLayers.LonLat(longitude_centro,latitude_centro).transform(from_proj, to_proj),icon));

	map.addControl(new OpenLayers.Control.LayerSwitcher());
	map.zoomToMaxExtent();
	map.setCenter (new OpenLayers.LonLat(longitude_centro, latitude_centro).transform(from_proj, to_proj), zoom);
}
