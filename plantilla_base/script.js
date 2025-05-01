fetch("config.json")
  .then(response => response.json())
  .then(data => {
    document.getElementById("nombre").textContent = data.nombre;
    document.getElementById("descripcion").textContent = data.descripcion;
    document.getElementById("logo").src = data.logo;

    const servicios = document.getElementById("servicios");
    data.servicios.forEach(s => {
      const li = document.createElement("li");
      li.textContent = s;
      servicios.appendChild(li);
    });

    const galeria = document.getElementById("galeria");
    data.imagenes.forEach(item => {
      const img = document.createElement("img");
      img.src = item.url;
      img.alt = item.nombre;
      img.title = item.nombre;
      galeria.appendChild(img);
    });

    document.getElementById("whatsapp").href = data.whatsapp;
    document.getElementById("instagram").href = data.instagram;
  });
