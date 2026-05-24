import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. PAGE CONFIGURATION & CUSTOM CSS
# ==========================================
st.set_page_config(page_title="NexTransit AI", page_icon="🚑", layout="wide", initial_sidebar_state="expanded")

# Injecting Custom CSS for a Cyber/High-Tech Aesthetic
custom_css = """
<style>
    /* Import modern tech font */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

    /* Apply font globally */
    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif !important;
    }

    /* Gradient Title */
    h1 {
        background: -webkit-linear-gradient(45deg, #00ff66, #00bfff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        letter-spacing: 1px;
    }

    /* Style the Metric Cards */
    [data-testid="stMetric"] {
        background-color: #12141a;
        border: 1px solid #2b2e36;
        border-top: 3px solid #00ff66;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 8px 25px rgba(0, 255, 102, 0.05);
        transition: transform 0.2s ease-in-out;
    }
    
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0, 255, 102, 0.15);
    }

    /* Style the Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0b0d12;
        border-right: 1px solid #1f232b;
    }

    /* Customizing success/error boxes */
    .stAlert {
        border-radius: 10px !important;
        border: none !important;
    }
    
    /* Horizontal Rule styling */
    hr {
        border-color: #2b2e36 !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR NAVIGATION & CONTROLS
# ==========================================
st.sidebar.markdown("<h2 style='text-align: center; color: #ffffff;'>🧭 COMMAND MENU</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("", ["🚥 Live Dashboard", "📖 About"])
st.sidebar.markdown("---")

if page == "🚥 Live Dashboard":
    st.sidebar.markdown("<h3 style='color: #00bfff;'>🕹️ Simulation Parameters</h3>", unsafe_allow_html=True)
    view_mode = st.sidebar.selectbox("Select Viewport Layer:", ["Micro-Simulation Canvas", "Live World Routing Map"])
    st.sidebar.markdown("---")
    traffic_density = st.sidebar.radio("Intersection Queue Density:", ["Low (5 Cars)", "Medium (15 Cars)", "Critical (40 Cars)"])
    ambulance_speed = st.sidebar.slider("Ambulance Velocity (km/h):", 30, 90, 60)
    sim_distance = st.sidebar.slider("Distance to Junction (Meters):", 50, 1000, 800)

    st.sidebar.markdown("---")
    st.sidebar.markdown("<h3 style='color: #ff3333;'>🚨 Incident Management</h3>", unsafe_allow_html=True)
    accident_active = st.sidebar.toggle("💥 Inject Major Hazard", value=False)

    crash_val = "true" if accident_active else "false"
    car_count = 5 if "Low" in traffic_density else (15 if "Medium" in traffic_density else 40)
    ambulance_tta = sim_distance / (ambulance_speed / 3.6)

# ==========================================
# PAGE 1: THE LIVE DASHBOARD
# ==========================================
if page == "🚥 Live Dashboard":
    
    # --- 3D HERO SECTION ---
    three_js_hero = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; overflow: hidden; background-color: #0b0d12; font-family: 'Segoe UI', sans-serif; pointer-events: none; }
            #canvas-container { width: 100vw; height: 300px; position: absolute; z-index: 1; pointer-events: none; }
            .hero-text { position: absolute; z-index: 2; top: 40%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: white; width: 100%; pointer-events: none; }
            h1 { font-size: 3.5rem; margin: 0; text-shadow: 0px 4px 30px rgba(0,255,102,0.8); letter-spacing: 3px; font-family: sans-serif; font-weight: 800; background: -webkit-linear-gradient(45deg, #00ff66, #00bfff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
            p { font-size: 1.2rem; color: #a0a0a0; margin-top: 10px; letter-spacing: 1px; }
            .scroll-hint { position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: #00ff66; font-size: 12px; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; animation: bounce 2s infinite; z-index: 2; border: 1px solid #00ff66; padding: 8px 16px; border-radius: 20px; background: rgba(0,255,102,0.1); }
            @keyframes bounce { 0%, 20%, 50%, 80%, 100% {transform: translateY(0) translateX(-50%);} 40% {transform: translateY(-10px) translateX(-50%);} 60% {transform: translateY(-5px) translateX(-50%);} }
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    </head>
    <body>
        <div id="canvas-container"></div>
        <div class="hero-text">
            <h1>NEXTRANSIT AI</h1>
            <p>Software-Defined Edge Preemption Twin</p>
        </div>
        <div class="scroll-hint">Engage Dashboard Below</div>
        <script>
            const scene = new THREE.Scene();
            scene.fog = new THREE.FogExp2(0x0b0d12, 0.005);
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 300, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
            renderer.setSize(window.innerWidth, 300);
            document.getElementById('canvas-container').appendChild(renderer.domElement);

            const geometry = new THREE.BufferGeometry();
            const vertices = [];
            for (let i = 0; i < 600; i++) {
                vertices.push(THREE.MathUtils.randFloatSpread(250), THREE.MathUtils.randFloatSpread(250), THREE.MathUtils.randFloatSpread(250));
            }
            geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
            const material = new THREE.PointsMaterial({ color: 0x00ff66, size: 1.8, transparent: true, opacity: 0.8 });
            const particles = new THREE.Points(geometry, material);
            scene.add(particles);

            const lineMaterial = new THREE.LineBasicMaterial({ color: 0x00bfff, transparent: true, opacity: 0.15 });
            const lineGeometry = new THREE.BufferGeometry().setFromPoints(
                new Array(100).fill().map(() => new THREE.Vector3(THREE.MathUtils.randFloatSpread(150), THREE.MathUtils.randFloatSpread(150), THREE.MathUtils.randFloatSpread(150)))
            );
            const lines = new THREE.LineSegments(lineGeometry, lineMaterial);
            scene.add(lines);

            camera.position.z = 80;
            function animate() { 
                requestAnimationFrame(animate); 
                particles.rotation.x += 0.0003; 
                particles.rotation.y += 0.0005; 
                lines.rotation.y -= 0.0004; 
                lines.rotation.x += 0.0002;
                renderer.render(scene, camera); 
            }
            animate();
        </script>
    </body>
    </html>
    """
    components.html(three_js_hero, height=300)
    
    # --- DYNAMIC METRICS & QUEUE ANALYTICS ---
    st.markdown("### 📊 Live System Telemetry")
    
    queue_drain_time = car_count * 2.2 
    safety_margin = ambulance_tta - queue_drain_time

    # ROW 1: Primary Asset Data
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="⏱️ Asset Velocity", value=f"{ambulance_speed} km/h", delta="Live Tracking")
    with col2:
        st.metric(label="🎯 Proximity to Node", value=f"{sim_distance} m", delta="Approaching", delta_color="inverse")
    with col3:
        if accident_active:
            st.error("🚨 STATUS: DETOUR ACTIVE")
        elif sim_distance < 400:
            st.success("🟢 STATUS: GREEN FLUSH")
        else:
            st.warning("🟡 STATUS: STANDBY MONITORING")
            
    st.markdown("<br>", unsafe_allow_html=True)
            
    # ROW 2: Advanced Preemption Data
    st.markdown("<h4 style='color: #a0a0a0;'>🚦 Preemption & Queue Analytics</h4>", unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.metric(label="⏳ Time to Arrival (TTA)", value=f"{ambulance_tta:.1f} sec", delta="Impact Window", delta_color="off")
    with col5:
        st.metric(label="🏎️ Queue Clear Time", value=f"{queue_drain_time:.1f} sec", delta=f"{car_count} Vehicles to Flush", delta_color="normal")
    with col6:
        if accident_active:
            st.metric(label="⚠️ Safety Margin", value="N/A", delta="Route Blocked", delta_color="inverse")
        elif safety_margin > 0:
            st.metric(label="✅ Safety Margin", value=f"+{safety_margin:.1f} sec", delta="Safe to Flush", delta_color="normal")
        else:
            st.metric(label="❌ Safety Margin", value=f"{safety_margin:.1f} sec", delta="Gridlock Warning - TTA Too Short", delta_color="inverse")
            
    st.markdown("---")

    # --- RENDER SELECTED VIEWPORT ---
    if view_mode == "Micro-Simulation Canvas":
        st.markdown("### 🚦 Intersection Micro-Simulator")

        html_canvas = f"""
        <div style="background-color:#12141a; padding:20px; border-radius:12px; border: 1px solid #1f232b; box-shadow:0 10px 40px rgba(0,0,0,0.5);">
            <canvas id="trafficCanvas" width="920" height="260" style="background-color:#0b0d12; display:block; border-radius:8px; margin: 0 auto; width: 100%; border: 1px solid #2b2e36;"></canvas>
        </div>

        <script>
            const canvas = document.getElementById('trafficCanvas');
            const ctx = canvas.getContext('2d');
            
            let currentDistance = {sim_distance};
            let baseVelocity = {ambulance_speed};
            let currentVelocity = baseVelocity;
            let isCrashActive = {crash_val};
            let totalCars = {car_count};
            
            const stopLineX = 700;
            const mainRoadY = 110; 

            function drawSimulationFrame() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                if (isCrashActive) {{
                    currentVelocity = 30.0;
                }} else if (currentDistance < 400) {{
                    currentVelocity = Math.min(90.0, baseVelocity + 20); 
                }} else {{
                    currentVelocity = baseVelocity; 
                }}

                let isOverrideActive = (currentDistance < 400 && !isCrashActive);
                let detourTurnX = Math.min(280, (stopLineX - (isOverrideActive ? 5 : 40) * 14) - 40);
                if(detourTurnX < 50) detourTurnX = 50;

                // Draw Roads
                ctx.fillStyle = '#1a1c23'; ctx.fillRect(0, mainRoadY, canvas.width, 60); 
                ctx.fillRect(stopLineX, 0, 70, canvas.height); 
                ctx.fillStyle = '#22252e'; ctx.fillRect(detourTurnX, 40, 50, mainRoadY - 40); 
                ctx.fillRect(detourTurnX, 20, stopLineX - detourTurnX + 45, 20); ctx.fillRect(stopLineX + 20, 20, 50, mainRoadY - 20); 

                // Draw Lane Markings
                ctx.strokeStyle = '#3d424f'; ctx.lineWidth = 2; ctx.setLineDash([12, 10]); ctx.beginPath();
                ctx.moveTo(0, mainRoadY + 30); ctx.lineTo(stopLineX, mainRoadY + 30);
                ctx.moveTo(stopLineX + 70, mainRoadY + 30); ctx.lineTo(canvas.width, mainRoadY + 30); ctx.stroke();
                ctx.setLineDash([]); ctx.lineWidth = 4; ctx.beginPath(); ctx.moveTo(stopLineX, mainRoadY); ctx.lineTo(stopLineX, mainRoadY + 60); ctx.stroke();

                let ambulanceX = stopLineX - currentDistance;
                let drawAmbX = ambulanceX;
                let drawAmbY = mainRoadY + 15; 
                
                if (isCrashActive && ambulanceX >= detourTurnX) {{
                    if (ambulanceX <= stopLineX + 40) {{
                        drawAmbX = Math.max(detourTurnX + 20, Math.min(ambulanceX, stopLineX + 40));
                        drawAmbY = 30; 
                        ctx.strokeStyle = '#00ff66'; ctx.lineWidth = 3; ctx.beginPath();
                        ctx.moveTo(detourTurnX + 25, mainRoadY + 15); ctx.lineTo(detourTurnX + 25, 30);
                        ctx.lineTo(stopLineX + 45, 30); ctx.lineTo(stopLineX + 45, mainRoadY + 15); ctx.stroke();
                    }} else {{
                        drawAmbX = ambulanceX; drawAmbY = mainRoadY + 15;
                    }}
                }}

                // Draw Ambulance
                ctx.fillStyle = '#ff007f'; ctx.fillRect(drawAmbX - 22, drawAmbY - 10, 28, 20);
                ctx.fillStyle = '#ffffff'; ctx.beginPath(); ctx.moveTo(drawAmbX + 6, drawAmbY - 10); ctx.lineTo(drawAmbX + 18, drawAmbY - 10); ctx.lineTo(drawAmbX + 12, drawAmbY + 10); ctx.lineTo(drawAmbX + 6, drawAmbY + 10); ctx.fill();
                ctx.fillStyle = '#00bfff'; ctx.fillRect(drawAmbX - 4, drawAmbY - 15, 8, 5); // Siren
                ctx.fillStyle = '#000'; ctx.beginPath(); ctx.arc(drawAmbX - 12, drawAmbY + 10, 4, 0, 2 * Math.PI); ctx.fill();
                ctx.beginPath(); ctx.arc(drawAmbX + 6, drawAmbY + 10, 4, 0, 2 * Math.PI); ctx.fill();

                // Draw Waiting Cars
                let visibleCars = isOverrideActive ? 0 : Math.min(totalCars, 12);
                let startQueueX = stopLineX - 20;
                for (let i = 0; i < visibleCars; i++) {{
                    let carX = startQueueX - (i * 26);
                    if (carX > 10) {{
                        ctx.fillStyle = '#4a5568'; ctx.fillRect(carX - 10, mainRoadY + 38, 20, 10);
                        ctx.fillStyle = '#2d3748'; ctx.beginPath(); ctx.moveTo(carX - 5, mainRoadY + 38); ctx.lineTo(carX + 4, mainRoadY + 38); ctx.lineTo(carX + 8, mainRoadY + 44); ctx.lineTo(carX - 8, mainRoadY + 44); ctx.fill();
                        ctx.fillStyle = '#111'; ctx.beginPath(); ctx.arc(carX - 6, mainRoadY + 48, 2.5, 0, 2 * Math.PI); ctx.fill(); ctx.beginPath(); ctx.arc(carX + 6, mainRoadY + 48, 2.5, 0, 2 * Math.PI); ctx.fill();
                    }}
                }}

                // Draw Traffic Light
                let signalColor = isCrashActive ? '#ffbb00' : (isOverrideActive ? '#00ff66' : '#ff3333'); 
                ctx.shadowBlur = 15; ctx.shadowColor = signalColor;
                ctx.fillStyle = signalColor; ctx.beginPath(); ctx.arc(stopLineX + 15, mainRoadY - 20, 12, 0, 2 * Math.PI); ctx.fill();
                ctx.shadowBlur = 0; ctx.lineWidth = 2; ctx.strokeStyle = '#fff'; ctx.stroke();
                
                if (isCrashActive) {{
                    ctx.fillStyle = '#ff3333'; ctx.font = '32px Arial'; ctx.fillText("💥", stopLineX + 35, mainRoadY + 35);
                }}

                // Animation Loop Logic
                if (currentDistance > -100) {{ 
                    currentDistance -= (currentVelocity / 150); 
                }} else {{ 
                    currentDistance = 950.0; 
                }}
                
                requestAnimationFrame(drawSimulationFrame);
            }}
            
            requestAnimationFrame(drawSimulationFrame);
        </script>
        """
        components.html(html_canvas, height=350)

    else:
        st.markdown("### 🌐 Global Routing Array (Greater Noida)")
        
        if accident_active:
            html_map_content = """
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
            <div id="map" style="width: 100%; height: 480px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.5); border: 2px solid #1f232b;"></div>
            <script>
                var map = L.map('map').setView([28.4595, 77.4991], 14);
                L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
                    attribution: '&copy; OpenStreetMap contributors &copy; CARTO'
                }).addTo(map);
                
                var ambIcon = L.divIcon({className: 'custom-div-icon', html: "<div style='font-size:24px;'>🚑</div>", iconSize: [30, 30], iconAnchor: [15, 15]});
                L.marker([28.4485, 77.4850], {icon: ambIcon}).addTo(map);
                L.circle([28.4595, 77.4991], {color: '#ff007f', fillColor: '#ff007f', fillOpacity: 0.4, radius: 200}).addTo(map).bindPopup('<b>HAZARD ZONE</b>').openPopup();
                
                L.polyline([[28.4485, 77.4850], [28.4680, 77.4920], [28.4710, 77.5120], [28.4520, 77.5250]], {color: '#00ff66', weight: 5, opacity: 0.8, dashArray: '10, 10'}).addTo(map);
            </script>
            """
        else:
            html_map_content = """
            <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
            <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
            <div id="map" style="width: 100%; height: 480px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.5); border: 2px solid #1f232b;"></div>
            <script>
                var map = L.map('map').setView([28.4595, 77.4991], 14);
                L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
                    attribution: '&copy; OpenStreetMap contributors &copy; CARTO'
                }).addTo(map);
                
                var ambIcon = L.divIcon({className: 'custom-div-icon', html: "<div style='font-size:24px;'>🚑</div>", iconSize: [30, 30], iconAnchor: [15, 15]});
                L.marker([28.4485, 77.4850], {icon: ambIcon}).addTo(map);
                
                L.polyline([[28.4485, 77.4850], [28.4595, 77.4991], [28.4520, 77.5250]], {color: '#00bfff', weight: 5, opacity: 0.8}).addTo(map);
            </script>
            """
            
        components.html(html_map_content, height=500)

# ==========================================
# PAGE 2: PROJECT DOCUMENTATION (ABOUT)
# ==========================================
elif page == "📖 About":
    
    st.markdown("<h1>About NexTransit AI</h1>", unsafe_allow_html=True)
    st.write("A next-generation software-defined ecosystem for emergency vehicle routing and traffic preemption.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🎯 The Problem & Our Mission")
        st.write(
            "Urban congestion is a critical bottleneck for emergency medical services. Every second an ambulance "
            "spends waiting at a red light or stuck behind traffic decreases the survival rate of the patient. "
            "Traditional systems rely on loud sirens or manual overrides, which are often too late to clear the path."
        )
        st.write(
            "**NexTransit AI** bridges this gap by transforming passive city infrastructure into an active, predictive "
            "command grid that clears intersections *before* the ambulance even arrives."
        )
        
    with col2:
        st.success("### ⚡ System Capabilities")
        st.write("NexTransit AI acts as a digital twin for city traffic management, capable of:")
        st.markdown(
            """
            * **Predictive Preemption:** Calculating exact Time-to-Arrival (TTA) based on dynamic asset velocity and distance.
            * **Automated Queue Flushing:** Forcing signal changes early enough to drain civilian traffic blocks, ensuring a zero-stop safety margin.
            * **Satellite-Level Rerouting:** Instantly calculating bypass paths and sending them to the driver when primary corridors are blocked by major hazards.
            * **Edge-AI Ready:** Architected to ingest real-world CCTV queue data and secure GPS telemetry arrays.
            """
        )

    st.markdown("---")
    st.markdown("### 🛠️ Technology Stack")
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    with tech_col1:
        st.markdown("#### Frontend Framework")
        st.markdown("`Streamlit` `HTML5 Canvas` `Three.js` `JS`")
        st.caption("Powers the high-performance, zero-flicker interactive dashboard and 3D node visuals.")
    with tech_col2:
        st.markdown("#### Core Logic & Routing")
        st.markdown("`Python` `Leaflet Maps` `CartoDB Tiles`")
        st.caption("Handles the backend TTA math, queue drain algorithms, and dynamic satellite pathfinding.")
    with tech_col3:
        st.markdown("#### Simulated Inputs")
        st.markdown("`Edge CCTV Streams` `GPS Telemetry`")
        st.caption("Emulates real-world data pipelines from municipal cameras and vehicle transponders.")