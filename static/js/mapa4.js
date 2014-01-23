 var map;
  function init() {    
    var options = {   
                      scales: [500, 1000, 2500, 5000, 10000],
                      numZoomLevels: 26,
                      allOverlays: true,
                      projection: new OpenLayers.Projection("EPSG:900913"),
                      displayProjection: new OpenLayers.Projection("EPSG:4326"),
                      controls:[
                        new OpenLayers.Control.Navigation(),
                        new OpenLayers.Control.PanZoomBar(),
                        new OpenLayers.Control.LayerSwitcher({'ascending':false}), 
                        new OpenLayers.Control.ScaleLine(),
                        new OpenLayers.Control.MousePosition(),
                        new OpenLayers.Control.OverviewMap(),
                        new OpenLayers.Control.Attribution(),
                        new OpenLayers.Control.KeyboardDefaults()],};


    map = new OpenLayers.Map('map_element', options);  

    var gsat = new OpenLayers.Layer.Google(
    "Google Satellite",
    {type: google.maps.MapTypeId.SATELLITE} );
    map.addLayer(gsat);
    gsat.mapObject.setTilt(0);            

    var kml = new OpenLayers.Layer.Vector("zahrada", {
                projection: map.displayProjection,
                strategies: [new OpenLayers.Strategy.Fixed()],
                protocol: new OpenLayers.Protocol.HTTP({
                    url: "kml/zahrada.kml",
                    format: new OpenLayers.Format.KML({
                        extractStyles: true,
                        extractAttributes: true,
                    })
                })  
            });

    map.addLayer(kml);     

    var vrstva_dve = new OpenLayers.Layer.Vector("vrstva_dve", {
                projection: map.displayProjection,
                strategies: [new OpenLayers.Strategy.Fixed()],
                protocol: new OpenLayers.Protocol.HTTP({
                    url: "kml/vrstva_dve.kml",
                    format: new OpenLayers.Format.KML({
                        extractStyles: true,
                        extractAttributes: true,
                    })
                })  
            });

    map.addLayer(vrstva_dve);

    select = new OpenLayers.Control.SelectFeature(kml); // here I tried ([kml, vrstva_dve]) , but still only layer kml is selectable 
            kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
            });
            map.addControl(select);
            select.activate();   

  function onPopupClose(evt) {
        select.unselectAll();
  }

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