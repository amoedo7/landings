const HeroSection = () => {
  return (
    <div className="relative h-screen flex items-center justify-center bg-black overflow-hidden">
      {/* Imagen de fondo */}
      <img 
        src="https://i.imgur.com/YsZz0VG.jpg" 
        alt="Background Proyecto Estampa" 
        className="absolute inset-0 w-full h-full object-cover opacity-30"
      />

      {/* Capa oscura encima para contraste */}
      <div className="absolute inset-0 bg-black opacity-60"></div>

      {/* Contenido principal */}
      <div className="relative z-10 text-center px-4 max-w-4xl mx-auto">
        {/* Logo con transparencia */}
   {/* Texto bordado animado */}
<div className="mb-8 stitching-text relative flex justify-center items-center">
  <div className="animate-typewriter">PROYECTO ESTAMPA</div>
  <div className="needle"></div>
</div>

        <h1 className="text-3xl md:text-4xl font-bold text-white mb-8 leading-tight">
          Transformamos prendas en <span className="text-amber-400">obras de arte</span> con técnicas profesionales
        </h1>
        <div className="flex flex-col sm:flex-row justify-center gap-4">
          {/* Botón WhatsApp */}
          <a 
            href="https://wa.me/qr/55J6JDCP2CJRN1" 
            className="bg-green-600 hover:bg-green-700 text-white px-8 py-4 rounded-full font-bold text-lg shadow-lg hover:shadow-xl transition-all duration-300 flex items-center justify-center gap-2"
          >
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"> ... </svg>
            WhatsApp
          </a>

          {/* Botón Instagram */}
          <a 
            href="https://www.instagram.com/proyectoestampa" 
            className="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white px-8 py-4 rounded-full font-bold text-lg shadow-lg hover:shadow-xl transition-all duration-300 flex items-center justify-center gap-2"
          >
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"> ... </svg>
            Instagram
          </a>
        </div>
      </div>
    </div>
  );
};


export default HeroSection;