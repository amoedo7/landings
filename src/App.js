import React from 'react';
import HeroSection from './components/HeroSection';
import ServicesSection from './components/ServicesSection';
import GallerySection from './components/GallerySection';
import AboutSection from './components/AboutSection';
import Footer from './components/Footer';

const App = () => {
  return (
    <div className="font-sans">
      <HeroSection />
      <ServicesSection />
      <GallerySection />
      <AboutSection />
      <Footer />
    </div>
  );
};

export default App;

// DONE