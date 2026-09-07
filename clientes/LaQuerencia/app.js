const PHONE='5492477331722';
const openWhatsApp=msg=>window.open(`https://wa.me/${PHONE}?text=${encodeURIComponent(msg)}`,'_blank','noopener');
document.querySelectorAll('.wa-action').forEach(el=>el.addEventListener('click',e=>{const msg=el.dataset.msg;if(!msg)return;e.preventDefault();openWhatsApp(msg)}));
const search=document.getElementById('plantSearch');
if(search){search.addEventListener('input',()=>{const q=search.value.toLowerCase().trim();document.querySelectorAll('#categoryGrid .cat').forEach(card=>{const hay=(card.dataset.search+' '+card.innerText).toLowerCase();card.classList.toggle('hidden',q&&!hay.includes(q));});});}
const form=document.getElementById('finderForm');
if(form){form.addEventListener('submit',e=>{e.preventDefault();const space=document.getElementById('space').value,light=document.getElementById('light').value,care=document.getElementById('care').value,goal=document.getElementById('goal').value;if(!space||!light||!care||!goal)return;openWhatsApp(`Hola La Querencia 🌿 Quiero que me recomienden una planta.\n\n• Lugar: ${space}\n• Luz: ${light}\n• Cuidados: ${care}\n• Busco: ${goal}\n\n¿Qué me recomiendan y qué tienen disponible?`);});}