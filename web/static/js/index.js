document.addEventListener("DOMContentLoaded", () => {
  const burger = document.querySelector(".navbar-burger");
  const menu = document.querySelector(".navbar-menu");
  const messageButtons =
    document.querySelectorAll(".notification .delete") || [];

  if (burger !== null) {
    burger.addEventListener("click", () => {
      burger.classList.toggle("is-active");
      menu.classList.toggle("is-active");
    });
  }

  messageButtons.forEach((button) => {
    const notification = button.parentNode;
    button.addEventListener("click", () =>
      notification.parentNode.removeChild(notification)
    );
  });
});
