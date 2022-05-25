$(document).ready(function(){
      var map = L.map('map').setView([51.154811, 71.419517], 12);

      L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoicmVuYXQyMDAxIiwiYSI6ImNrdXNtZGxobTBnNGYydW1mOTdkMTlwemwifQ.sb_Eehw7l4HREZ6vnUiVGA', {
          attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          maxZoom: 18,
          id: 'mapbox/streets-v11',
          tileSize: 512,
          zoomOffset: -1,
          accessToken: 'pk.eyJ1IjoicmVuYXQyMDAxIiwiYSI6ImNrdXNtZGxobTBnNGYydW1mOTdkMTlwemwifQ.sb_Eehw7l4HREZ6vnUiVGA'
      }).addTo(map);

      var raw_data = '{{ place|escapejs }}';
      var m_data = malls

      var mallsLayer = L.geoJSON(malls, {
        style: style,
        onEachFeature: onEachFeature
      }).bindPopup(function (layer) {
          sidebar.show();
          sidebar.setContent("<table>"
                             + displayContent(layer.feature.properties)
                             + "</table>");
      }).addTo(map);

      // Interaction
      function style(feature) {
          return {
              fillColor: '#f9429e',
              weight: 2,
              opacity: 1,
              color: 'white',
              dashArray: '3',
              fillOpacity: 0.7
          };
      }

      function highlightFeature(e) {
          var layer = e.target;

          layer.setStyle({
              weight: 5,
              color: '#666',
              dashArray: '',
              fillOpacity: 0.7
          });

          if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
              layer.bringToFront();
          }
      }

      function resetHighlight(e) {
          mallsLayer.resetStyle(e.target);
      }

      function zoomToFeature(e) {
          map.fitBounds(e.target.getBounds());
      }

      function onEachFeature(feature, layer) {
          layer.on({
              mouseover: highlightFeature,
              mouseout: resetHighlight,
              click: zoomToFeature
          });
      }

      // Sidebar

      var sidebar = L.control.sidebar('sidebar', {
          closeButton: true,
          position: 'left'
      });

      map.addControl(sidebar);

      map.on('click', function () {
            sidebar.hide();
      })


      // map.on('click', onMapClick);

    })