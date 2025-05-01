const AboutSection = () => {
  return (
    <div className="py-20 bg-white">
      <div className="container mx-auto px-4">
        <div className="flex flex-col lg:flex-row items-center gap-12">
          <div className="lg:w-1/2">
            <div className="text-center lg:text-left mb-8">
              <h2 className="text-4xl font-bold text-gray-900 mb-4">Quiénes Somos</h2>
              <div className="w-24 h-1 bg-amber-500 mx-auto lg:mx-0"></div>
            </div>
            <p className="text-lg text-gray-700 mb-6">
              En Proyecto Estampa nos especializamos en transformar prendas en piezas únicas mediante técnicas de estampado profesional. Cada trabajo refleja nuestra pasión por el detalle y la calidad.
            </p>
            <div className="space-y-4">
              <div className="flex items-start">
                <svg className="w-6 h-6 text-amber-500 mt-1 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                </svg>
                <div>
                  <h3 className="font-semibold text-gray-900">Nuestro Taller</h3>
                  <p className="text-gray-600">Raimundo R. 1493, Pergamino, Provincia de Buenos Aires</p>
                </div>
              </div>
            </div>
          </div>
          <div className="lg:w-1/2 h-96 rounded-xl overflow-hidden shadow-lg">
            <iframe 
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3313.041086598467!2d-60.5739239241366!3d-33.8679176732405!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95b9a7d6a3d7b3e5%3A0x3a3a3a3a3a3a3a3a!2sRaimundo%20R.%201493%2C%20Pergamino%2C%20Provincia%20de%20Buenos%20Aires!5e0!3m2!1ses!2sar!4v1620000000000!5m2!1ses!2sar" 
              width="100%" 
              height="100%" 
              style={{border:0}} 
              allowFullScreen="" 
              loading="lazy"
            ></iframe>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AboutSection;