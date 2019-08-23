document.addEventListener("DOMContentLoaded", function()
{
    document.querySelectorAll(".item-list").forEach(function(button)
    {
        button.onclick = function()
        {
            var placeholder = document.querySelector("#notification_placeholder");

            placeholder.innerHTML =
                `<div class="alert alert-danger text-center" id="notification">
                    <span>Sorry, you need to log in to order item!</span>
                </div>`;

            setTimeout(function()
            {
                placeholder.innerHTML = "";
            }, 4000);

            return false;
        };
    });
});
