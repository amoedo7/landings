const GallerySection = () => {
  const media = [
    { type: 'image', src: 'https://i.imgur.com/I8Pyd8h.jpg' },
    { type: 'video', src: 'https://i.imgur.com/3pRALtL.mp4' },
    { type: 'image', src: 'https://i.imgur.com/AjvCRpU.jpg' },
    { type: 'video', src: 'https://i.imgur.com/KnvZJeg.mp4' },
    { type: 'image', src: 'https://i.imgur.com/MhqyJrK.jpg' },
    { type: 'video', src: 'https://i.imgur.com/6ozoHht.mp4' }
  ];

  return (
    <div className="py-20 bg-gray-100">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-bold text-gray-900 mb-4">Nuestros Trabajos</h2>
          <div className="w-24 h-1 bg-amber-500 mx-auto"></div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {media.map((item, index) => (
            <div key={index} className="rounded-xl overflow-hidden shadow-lg bg-white hover:shadow-xl transition-shadow duration-300">
              {item.type === 'image' ? (
                <img 
                  src={item.src} 
                  alt="Trabajo de Proyecto Estampa" 
                  className="w-full h-64 object-cover"
                />
              ) : (
                <video 
                  autoPlay 
                  loop 
                  muted 
                  playsInline
                  className="w-full h-64 object-cover"
                >
                  <source src={item.src} type="video/mp4" />
                </video>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default GallerySection;