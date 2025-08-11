const API_BASE = 'https://{api-id}.execute-api.{region}.amazonaws.com/Prod';

async function fetchItems(){
  const res = await fetch(`${API_BASE}/items`);
  const items = await res.json();
  const ul = document.getElementById('list');
  ul.innerHTML = '';
  items.forEach(i=>{
    const li = document.createElement('li');
    li.textContent = `${i.title} [${i.completed}]`;
    ul.appendChild(li);
  })
}

document.getElementById('add').addEventListener('click', async ()=>{
  const title = document.getElementById('title').value;
  await fetch(`${API_BASE}/items`, {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({title})
  });
  fetchItems();
});

fetchItems();
