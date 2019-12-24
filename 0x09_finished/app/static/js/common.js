/**
 * Created by hacker on 2017/10/15.
 */

$(function() {
  const posts_div = document.querySelector("#posts");

  fetch("/api/posts")
    .then(function(response) {
      return response.json();
    })
    .then(function(posts) {
      $.each(posts.results, function(index, post) {
        console.log(post);
        let item =
          '<article class="blog-post">' +
          "<header>" +
          "<h2>" +
          post.user_name +
          "</h2>" +
          "</header>" +
          "<div>" +
          '<img class="image" src="/images/' +
          post.image +
          '">' +
          "</div>" +
          "<div>" +
          "<p>" +
          post.text +
          "</p>" +
          "</div>" +
          "</article>";

        posts_div.insertAdjacentHTML("beforeend", item);
      });
    });
});
