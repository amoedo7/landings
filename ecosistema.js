const filters = [...document.querySelectorAll('.filter')];
const offices = [...document.querySelectorAll('.office')];

const officeAnchors = {
  'EstructurAMO': 'estructuramo',
  'IAMO / DAMO': 'iamo-damo',
  'DesarrolloAMO': 'desarrolloamo',
  'WebAMO': 'webamo',
  'DatabaseAMO': 'databaseamo',
  'SecurityAMO': 'securityamo',
  'InfraAMO': 'infraamo',
  'OperAMO': 'operamo',
  'MarketingAMO': 'marketingamo',
  'ContaduríaAMO': 'contaduriaamo',
  'InvestigAMO': 'investigamo',
  'CobrAMO': 'cobramo',
  'RagtAMO': 'ragtamo',
  'VideAMO': 'videamo',
  'CamarAMO': 'camaramo',
  'ChoferAMO': 'choferamo'
};

offices.forEach((office) => {
  const title = office.querySelector('h3')?.textContent.trim();
  const anchor = officeAnchors[title];
  if (!anchor) return;
  const link = document.createElement('a');
  link.href = `./oficinas.html#${anchor}`;
  link.className = 'office-link';
  link.textContent = 'Ver oficina →';
  office.querySelector('div')?.appendChild(link);
});

filters.forEach((button) => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    filters.forEach((item) => item.classList.toggle('is-active', item === button));
    offices.forEach((office) => {
      const visible = filter === 'all' || office.dataset.group === filter;
      office.classList.toggle('is-hidden', !visible);
    });
  });
});

const reveal = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.animate(
      [
        { opacity: 0, transform: 'translateY(16px)' },
        { opacity: 1, transform: 'translateY(0)' }
      ],
      { duration: 480, easing: 'cubic-bezier(.2,.8,.2,1)', fill: 'both' }
    );
    reveal.unobserve(entry.target);
  });
}, { threshold: 0.08 });

document.querySelectorAll('.office, .principles article, .participation-grid article').forEach((element) => reveal.observe(element));
