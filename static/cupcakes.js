$(".delete-cupcake").click(deleteCupcake);

async function deleteCupcake() {
  const id = $(this).data("id");
  await axios.delete(`/api/cupcakes/${id}`);
  $(this).parent().remove();
}

$(".create_cupcake_btn").click((event) => {
  event.preventDefault();
  createCupcake();
});

async function createCupcake() {
  const flavor = $("#flavor").val();
  const size = $("#size").val();
  const rating = $("#rating").val();
  const image = $("#image").val();

  const data = {
    flavor,
    size,
    rating,
    image,
  };
  const response = await axios.post("/api/cupcakes", data);

  const newCupcake = response.data.cupcake;
  $("ul").append(
    `<li>${newCupcake.flavor} - <button class="delete-cupcake" data-id="${newCupcake.id}">X</button></li>`
  );
  console.log(newCupcake);
}
