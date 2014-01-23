var map;

function init() {

        map = new OpenLayers.Map('mapa', {
                controls:[
                new OpenLayers.Control.Navigation(),
                new OpenLayers.Control.PanZoomBar(),
                new OpenLayers.Control.LayerSwitcher({'ascending':false}),
                new OpenLayers.Control.ScaleLine(),
                new OpenLayers.Control.MousePosition(),
                new OpenLayers.Control.OverviewMap(),
                new OpenLayers.Control.Attribution(),
                new OpenLayers.Control.KeyboardDefaults(),
                ]
        });
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
                        "http://a.tiles.mapbox.com/v3/inaebatistoni.map-t89cxkrw/${z}/${x}/${y}.png",
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

        var escola_kml = new OpenLayers.Layer.Vector('Escolas', {
                projection: map.displayProjection,
                strategies: [new OpenLayers.Strategy.Fixed()],
                protocol: new OpenLayers.Protocol.HTTP({
                        url: '/escola/kml_escolas/' + codigo_ibge + '/',
                        format: new OpenLayers.Format.KML({
                                extractStyles: true,
                                extractAttributes: true
                        })
                })
        });

        // KML fim

        // Plotagem das bibliotecas

        var bibliotecas_kml = new OpenLayers.Layer.Vector('Bibliotecas', {
        	projection: map.displayProjection,
        	visibility: false,
        	strategies: [new OpenLayers.Strategy.Fixed()],
        	protocol: new OpenLayers.Protocol.HTTP({
        		url: '/biblioteca/kml_bibliotecas/' + codigo_ibge + '/',
        		format: new OpenLayers.Format.KML({
        			extractStyles: true,
        			extractAttributes: true
        		})
        	})
        });

        // Plotagem das cras

        var cras_kml = new OpenLayers.Layer.Vector('CRAS', {
        	projection: map.displayProjection,
        	visibility: false,
        	strategies: [new OpenLayers.Strategy.Fixed()],
        	protocol: new OpenLayers.Protocol.HTTP({
        		url: '/cra/kml_cras/' + codigo_ibge + '/',
        		format: new OpenLayers.Format.KML({
        			extractStyles: true,
        			extractAttributes: true
        		})
        	})
        });

        // Plotagem das museus

        var museus_kml = new OpenLayers.Layer.Vector('Museus', {
            projection: map.displayProjection,
            visibility: false,
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: '/museu/kml_museu/' + codigo_ibge + '/',
                format: new OpenLayers.Format.KML({
                    extractStyles: true,
                    extractAttributes: true
                })
            })
        });

        // Plotagem dos equipamentos saude

        var saude_kml = new OpenLayers.Layer.Vector('Equip. Saude', {
            projection: map.displayProjection,
            visibility: false,
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: '/saude/kml_saude/' + codigo_ibge + '/',
                format: new OpenLayers.Format.KML({
                    extractStyles: true,
                    extractAttributes: true
                })
            })
        });

        // Plotagem dos cinemas

        var cinema_kml = new OpenLayers.Layer.Vector('Cinemas', {
            projection: map.displayProjection,
            visibility: false,
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: '/cinema/kml_cinema/' + codigo_ibge + '/',
                format: new OpenLayers.Format.KML({
                    extractStyles: true,
                    extractAttributes: true
                })
            })
        });

        // Plotagem dos teatros

        var teatro_kml = new OpenLayers.Layer.Vector('Teatros', {
            projection: map.displayProjection,
            visibility: false,
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: '/teatro/kml_teatro/' + codigo_ibge + '/',
                format: new OpenLayers.Format.KML({
                    extractStyles: true,
                    extractAttributes: true
                })
            })
        });

        // Plotagem dos centros de ciencia

        var centro_ciencia_kml = new OpenLayers.Layer.Vector('Centros Ciencia', {
            projection: map.displayProjection,
            visibility: false,
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: '/centro_ciencia/kml_centro_ciencia/' + codigo_ibge + '/',
                format: new OpenLayers.Format.KML({
                    extractStyles: true,
                    extractAttributes: true
                })
            })
        });

        // Plotagem das salas verdes

        var sala_verde_kml = new OpenLayers.Layer.Vector('Salas Verdes', {
            projection: map.displayProjection,
            visibility: false,
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: '/sala_verde/kml_sala_verde/' + codigo_ibge + '/',
                format: new OpenLayers.Format.KML({
                    extractStyles: true,
                    extractAttributes: true
                })
            })
        });

        // Plotagem pontos de cultura

        var ponto_cultura_kml = new OpenLayers.Layer.Vector('Pontos de Cultura', {
            projection: map.displayProjection,
            visibility: false,
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: '/ponto_cultura/kml_ponto_cultura/' + codigo_ibge + '/',
                format: new OpenLayers.Format.KML({
                    extractStyles: true,
                    extractAttributes: true
                })
            })
        });


        map.addLayers([
                mapbox,
                osm_layer,
                layer1,
                escola_kml,
                bibliotecas_kml,
                museus_kml,
                saude_kml,
                cras_kml,
                cinema_kml,
                teatro_kml,
                centro_ciencia_kml,
                sala_verde_kml,
                ponto_cultura_kml,

        ]);

        // POPUP KML inicio

        select = new OpenLayers.Control.SelectFeature([escola_kml, 
            bibliotecas_kml,
            museus_kml,
            saude_kml,
            cras_kml,
            cinema_kml,
            teatro_kml,
            centro_ciencia_kml,
            sala_verde_kml,
            ponto_cultura_kml,
            ]);

        escola_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        bibliotecas_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        museus_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        saude_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        cras_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        cinema_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        teatro_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        centro_ciencia_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        sala_verde_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        ponto_cultura_kml.events.on({
                "featureselected": onFeatureSelect,
                "featureunselected": onFeatureUnselect
        });

        map.addControl(select);
        select.activate();

        // POPUP KML fim

        map.addControl(new OpenLayers.Control.LayerSwitcher({}));
        map.setCenter (new OpenLayers.LonLat(longitude_centro, latitude_centro).transform(from_proj, to_proj), zoom);

        if(!map.getCenter()) {
                map.zoomToMaxExtent();
        }

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