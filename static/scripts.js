// JAVASCRIPT KODAS DINAMIŠKAI GENERUOTI LENTELĘ SU DUOMENIMIS
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/automobiliai')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('projektai-body');
            tbody.innerHTML = '';

            data.forEach(automobilis => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${automobilis.id}</td>
                    <td>${automobilis.gamintojas}</td>
                    <td>${automobilis.modelis}</td>
                    <td>${automobilis.kaina}</td>
                    <td>${automobilis.kainaPVM}</td>
                    <td>${automobilis.sukurimo data}</td>
                `;

                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

