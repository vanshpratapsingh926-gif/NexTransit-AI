# 🚑 NexTransit AI: Software-Defined Edge Preemption Twin

NexTransit AI is a high-performance smart-city digital twin designed to minimize emergency vehicle response times. By transforming passive traffic data channels into an active, predictive command matrix, the system clears intersection roadblocks autonomously before the asset arrives.
<br>

<video src="demo.mp4" controls="controls" width="100%">
</video>

<br>

## 🎯 Core Capabilities
* **Predictive Preemption Matrix:** Calculates real-time Time-to-Arrival (TTA) boundaries based on dynamic asset velocity mapping.
* **Intelligent Queue Flushing:** Estimates vehicle clearance windows using local density parameters to maintain a zero-stop safety margin.
* **Dynamic Satellite Detour Routing:** Instantly overrides localized signal paths and recalculates open-source bypass routes during major corridor incidents.

## 🛠️ Architecture & Tech Stack
* **UI/UX Layer:** Streamlit, custom injected CSS cyber-panel layout.
* **Graphics Engines:** Three.js (3D network nodes), HTML5 Canvas (2D micro-simulation array).
* **Geospatial Processing:** Leaflet.js mapped to CartoDB dark-matter tile topologies.
* **Core Logic Optimization:** Python-based telemetry parsing and queue drainage math modules.

## ⚙️ Engineering Paradigm (Why I Built It This Way)
Instead of relying on heavy server-side processing, this project leverages a **decoupled front-end execution strategy**. By offloading the visual loops to front-end browser memory via Javascript's `requestAnimationFrame` and rendering within an isolated canvas container, the dashboard completely eliminates Streamlit's native screen-refresh stuttering. This guarantees an ultra-low latency, zero-flicker desktop experience designed to emulate a real-world edge command room.

---
*Engineered as a flagship architectural prototype for urban telemetry optimization.*
