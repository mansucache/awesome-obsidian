// Local catalog search; filter state can be shared through the URL.
(() => {
  const search = document.querySelector('#search');
  const category = document.querySelector('#category');
  const price = document.querySelector('#price');
  const topic = document.querySelector('#topic');
  const records = [...document.querySelectorAll('[data-record]')];
  const count = document.querySelector('#count');
  const empty = document.querySelector('#empty');
  const normalize = value => value.normalize('NFKC').toLocaleLowerCase().trim();
  function update(save = true) {
    const terms = normalize(search.value).split(/\s+/).filter(Boolean);
    let found = 0;
    for (const record of records) {
      const matches = (!category.value || record.dataset.category.split(' ').includes(category.value)) &&
        (!topic.value || record.dataset.topic === topic.value) &&
        (!price.value || record.dataset.price === price.value) &&
        terms.every(term => normalize(record.dataset.search).includes(term));
      record.hidden = !matches;
      if (matches) found++;
    }
    const suffix = found === 1 && count.dataset.suffix === 'results' ? 'result' : count.dataset.suffix;
    count.textContent = `${found} ${suffix}`;
    empty.hidden = found !== 0;
    if (save) {
      const params = new URLSearchParams();
      for (const [key, field] of [['q',search],['category',category],['topic',topic],['price',price]]) {
        if (field.value) params.set(key, field.value);
      }
      const query = params.size ? `?${params}` : '';
      history.replaceState(null, '', `${location.pathname}${query}${location.hash}`);
    }
    const languageLink = document.querySelector('a[hreflang]');
    const other = new URL(languageLink.href);
    other.search = location.search;
    other.hash = location.hash;
    languageLink.href = other.href;
  }
  function applyURL() {
    const params = new URLSearchParams(location.search);
    search.value = params.get('q') || '';
    for (const [key, field] of [['category',category],['topic',topic],['price',price]]) {
      const value = params.get(key) || '';
      field.value = [...field.options].some(option => option.value === value) ? value : '';
    }
    update(false);
  }
  search.addEventListener('input', () => update());
  category.addEventListener('change', () => { topic.value = ''; update(); });
  topic.addEventListener('change', () => { category.value = ''; update(); });
  price.addEventListener('change', () => update());
  window.addEventListener('popstate', applyURL);
  document.querySelector('#reset').addEventListener('click', () => {
    search.value = ''; category.value = ''; price.value = ''; topic.value = '';
    history.replaceState(null, '', location.pathname);
    update(); search.focus();
  });
  applyURL();
})();
