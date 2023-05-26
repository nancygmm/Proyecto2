function submitForm() {

    var rating = [document.getElementById('movie1-rating').value , document.getElementById('movie2-rating').value, document.getElementById('movie3-rating').value, document.getElementById('movie4-rating').value, document.getElementById('movie5-rating').value, document.getElementById('movie6-rating').value, document.getElementById('movie7-rating').value, document.getElementById('movie8-rating').value, document.getElementById('movie9-rating').value, document.getElementById('movie10-rating').value, document.getElementById('movie11-rating').value, document.getElementById('movie12-rating').value, document.getElementById('movie13-rating').value, document.getElementById('movie14-rating').value, document.getElementById('movie15-rating').value, document.getElementById('movie16-rating').value, document.getElementById('movie17-rating').value, document.getElementById('movie18-rating').value, document.getElementById('movie19-rating').value, document.getElementById('movie20-rating').value]

    var peliculas = ['scary movie', 'mujer bonita', 'El señor de los anillos: La comunidad del anillo', 'El curioso caso de Benjamin Button', 'Interestelar', 'el rey leon', 'up', 'coco', 'inception', 'Black swan', 'El laberinto del fauno', 'Wall-E', 'El gran hotel Budapest', 'El silencio de los corderos', 'La princesa mononoke', 'El origen', 'El viaje de chihiro', 'La santa pascua', 'men on wire','x files']

    var portadas = ["../../static/accounts/scarymovie.jpg","../../static/accounts/prettywoman.jpg","../../static/accounts/senordelosanillos.jpg","../../static/accounts/benajaminbutton.jpg","../../static/accounts/interestelar.jpg","../../static/accounts/reyleon.jpg","../../static/accounts/up.jpg","../../static/accounts/coco.jpg","../../static/accounts/inception.jpg","../../static/accounts/blackswan.jpg","../../static/accounts/laberinto.jpg","../../static/accounts/walle.jpg","../../static/accounts/budapest.jpg","../../static/accounts/thelambs.jpg","../../static/accounts/mononoke.jpg","../../static/accounts/inception.jpg","../../static/accounts/chihiro.jpg","../../static/accounts/hop.jpg","../../static/accounts/manonwire.jpg","../../static/accounts/xflies.jpg"]

    var total = 0; 

    const datos = [];

    for (var i = 0; i < rating.length; i++) {
        if (rating[i] > 0) {
            var nuevoElemento = [peliculas[i],rating[i]]
            datos.push(nuevoElemento);
            total ++;
    }
    if (total > 3 | total < 3) {
      alert('Por favor, seleccione una calificacion para 3 peliculas.');
    return;
    }
    
    function crearCSV(datos) {
        // Crear el contenido del archivo CSV
        let contenidoCSV = '';
        datos.forEach((fila) => {
          contenidoCSV += fila.join(',') + '\n';
        });
      
        // Crear un objeto Blob
        const blob = new Blob([contenidoCSV], { type: 'text/csv' });
      
        // Crear un enlace de descarga
        const enlaceDescarga = document.createElement('a');
        enlaceDescarga.href = URL.createObjectURL(blob);
        enlaceDescarga.download = 'datos.csv';
      
        // Simular clic en el enlace para iniciar la descarga
        enlaceDescarga.click();
      }
      
      
      crearCSV(datos);
    // Aquí puedes hacer cualquier acción necesaria con las calificaciones seleccionadas
  
    document.getElementById('rating-form').submit();
}


}

