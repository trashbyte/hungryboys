$(function() {
  $(".header .title").each((i,e) => {
    e.innerHTML = e.innerText.split(".").slice(-1);
  });

  $("td.memname").each((i,e) => {
    e.innerHTML = e.innerText.split(".").slice(-1);
  });

  $("table.memname td").each((i,e) => {
    e.innerHTML = e.innerHTML.replace("&nbsp;","");
  });

  let breadcrumbs = $(".navelem");
  breadcrumbs = breadcrumbs.slice(0, breadcrumbs.length-1); // all but last
  $("<li>&gt;</li>").insertAfter(breadcrumbs);
});
