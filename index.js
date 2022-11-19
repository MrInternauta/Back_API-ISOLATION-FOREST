let fetchData = async () => {
  fetch('http://127.0.0.1:5000/calculateAnomaly').
    then(async res => {
      let data = await res.json();
      let obj = JSON.parse(data['data']);
    console.log((obj.amount) ?? 'error')
  })
}
fetchData()