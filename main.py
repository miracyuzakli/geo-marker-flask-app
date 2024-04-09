import streamlit as st
import streamlit.components.v1 as components
import folium
from streamlit_folium import folium_static

# Başlangıç koordinatları (Kanada üzerinde bir nokta)
start_coords = (56.130366, -106.346771)

# Folium haritasını oluşturma
m = folium.Map(location=start_coords, zoom_start=4)

# Haritayı Streamlit'e ekleme
map_html = folium_static(m, width=700, height=500)

# JavaScript ile tıklama olaylarını yakalama
clicks = st.session_state.get("clicks", [])

if not clicks:
    clicks = []
    st.session_state.clicks = clicks

# Haritada tıklama yapılınca çalışacak JavaScript kodu
js = """
<script>
    const map = document.querySelector('.folium-map');
    map.addEventListener('click', (event) => {
        window.parent.postMessage({
            type: 'map_click',
            coordinates: [event.latLng.lat, event.latLng.lng]
        }, '*');
    });
</script>
"""

# JavaScript kodunu sayfaya ekleme
components.html(js, height=0, width=0)

# Tıklama olaylarını yakalama
query_params = st.experimental_get_query_params()
if "map_click" in query_params:
    lat, lon = query_params["map_click"]
    clicks.append((float(lat), float(lon)))
    st.session_state.clicks = clicks

# Kullanıcının seçtiği noktaları göster
if st.button('Seçilen Noktaları Göster'):
    if len(clicks) >= 4:
        st.write("Seçilen Noktalar:")
        for i, click in enumerate(clicks[:4]):
            st.write(f"Nokta {i+1}: {click}")
    else:
        st.warning("Lütfen en az 4 nokta seçin.")
