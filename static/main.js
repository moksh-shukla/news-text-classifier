const input = document.querySelector(".urlinput");
const button = document.querySelector(".submitbtn");
const result = document.querySelector("#result");

/** Send network request to browser to fetch predicted class by URL */
const getPredictedClass = async (url) => {
  const response = await fetch("/predict?url=" + url);
  return response.text();
};

/** Event listener on the "Predict" button */
button.addEventListener("click", async () => {
  const url = input.value;
  button.disabled = true;
  button.innerHTML = "Predicting...";
  result.innerHTML = "";
  const predictedClass = await getPredictedClass(url);
  button.disabled = false;
  button.innerHTML = "Predict";
  if(predictedClass === "error") {
    result.innerHTML = "Invalid URL!! Please Try Again..";
  } 
  else {
    result.innerHTML = "Predicted class: " + predictedClass;
  }
});
