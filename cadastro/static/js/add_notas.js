document.addEventListener('DOMContentLoaded', function(){
  const somaInput = document.getElementById('soma')
  const unidades = document.querySelectorAll("input[type=number]");

  unidades.forEach(unidade => {
    unidade.addEventListener('focus', event => {
      // remove o valor anterior digitado da soma caso o usuario digite um novo valor
      if(event.target.value != ''){
        let valorAntigo = event.target.value

        unidade.addEventListener('change', e => {
          somaInput.value = (parseFloat(somaInput.value) - parseFloat(valorAntigo))
        })
      }

      event.target.addEventListener('change', displaySoma)
      event.target.addEventListener('change', displayMedia)
      
    })
  })

})

function displayMedia(e){
  const somaInput = document.getElementById('soma').value
  const mediaInput = document.getElementById('media')

  let media = parseFloat(somaInput)/4
  mediaInput.value = media.toFixed(1)
}

function displaySoma(e){
  const somaInput = document.getElementById('soma')

  if(somaInput.value == ''){
    somaInput.value = e.target.value
  }
  else{''
    let soma = parseFloat(somaInput.value) + parseFloat(e.target.value)
    somaInput.value = soma.toFixed(2)
  }
}