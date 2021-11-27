const compra = new Carrito();
const listaCompra = document.querySelector('#lista-compra tbody');
const carrito2 = document.getElementById('carrito');
const procesarCompraBtn = document.getElementById('procesar-compra');


cargarEventos();

function cargarEventos(){
    document.addEventListener('DOMContentLoaded', compra.leerLocalStorageCompra());
    carrito2.addEventListener('click', (e)=>{compra.eliminarProducto(e)});
    compra.calcularTotal();
    procesarCompraBtn.addEventListener('click', procesarCompra);
}

