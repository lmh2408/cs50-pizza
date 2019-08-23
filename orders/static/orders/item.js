document.addEventListener("DOMContentLoaded", function()
{
    document.querySelectorAll(".item-list").forEach(function(button)
    {
        button.onclick = function()
        {
            if (this.dataset["topping"] != "0")
            {
                var topping_number = Number(this.dataset["topping"]);
                console.log(topping_number);

                var list_diplay = document.querySelector("#list_diplay");

                const request = new XMLHttpRequest();
                request.open("GET", "/orders/pizza_topping");
                request.onload = function()
                {
                    const response = JSON.parse(request.responseText);
                    console.log(response);

                    list_diplay.innerHTML = "";

                    for (let i = 0, l = response["topping_list"].length; i < l; i++)
                    {
                        list_diplay.insertAdjacentHTML("beforeend",
                        `
                            <div class="row justify-content-center mb-1">
                                <div href="#" class="col-10 col-md-4 topping-list">
                                    <div class="row">
                                        <div class="col pl-3 py-1">
                                            <label for="${response["topping_list"][i]}">
                                                <input class="topping_check" name="topping" type="checkbox" id="${response["topping_list"][i]}" value="${response["topping_list"][i]}">
                                                <span>${response["topping_list"][i]}</span>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        `);
                    }

                };
                request.send();

                // var limit = topping_number;
                // $('input.topping_check').on('change', function(evt)
                // {
                //     if($(this).siblings(':checked').length >= limit)
                //     {
                //         this.checked = false;
                //     }
                // });

            }

        };
    });
});
