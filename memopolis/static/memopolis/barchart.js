const title_data_from_template = document.querySelector("#title-data")
.innerText.replace("['","")
.replace("']","")
.split("', '")
console.log(title_data_from_template)

const like_data_from_template = JSON.parse(document
.querySelector("#like-data").innerText)
console.log(like_data_from_template)


new Chart(document.getElementById("bar-chart"), {
    type: 'bar',
    data: {
      labels: title_data_from_template,
      datasets: [
        {
          label: "Punkty",
          backgroundColor: "rgb(91, 223, 91)",
          data: like_data_from_template
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Twoje punkty'
      }
    }
});
