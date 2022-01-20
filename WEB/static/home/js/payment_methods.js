const checkout_public_key = "{{checkout_public_key}}";
const checkout_session_id_subscription = "{{checkout_session_id_subscription}}";
const checkout_session_id_one_time = "{{checkout_session_id_one_time}}";
var stripe = Stripe(checkout_public_key);
const button_onetime = document.querySelector("#onetime");
const button_subscription = document.querySelector("#subscription");
button_onetime.addEventListener("click", (event) => {
  stripe
    .redirectToCheckout({
      sessionId: checkout_session_id_one_time,
    })
    .then(function (result) {});
});
button_subscription.addEventListener("click", (event) => {
  stripe
    .redirectToCheckout({
      sessionId: checkout_session_id_subscription,
    })
    .then(function (result) {});
});
