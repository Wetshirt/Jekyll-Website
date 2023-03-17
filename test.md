---
layout: default
---

<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <!-- Bootstrap -->
    <link rel="stylesheet" href="plugins/bootstrap/bootstrap.min.css">
    <!-- Bootstrap js-->
    <link rel="stylesheet" href="plugins/bootstrap/bootstrap.min.js">

    <!-- add after bootstrap.min.css -->
    <link
      rel="stylesheet"
      href="https://cdn.rawgit.com/afeld/bootstrap-toc/v1.0.1/dist/bootstrap-toc.min.css"
    />
    <!-- add after bootstrap.min.js or bootstrap.bundle.min.js -->
    <script src="https://cdn.rawgit.com/afeld/bootstrap-toc/v1.0.1/dist/bootstrap-toc.min.js"></script>
  </head>

  <body data-spy="scroll" data-target="#toc">
    <div class="container">
      <div class="row">
        <!-- sidebar, which will move to the top on a small screen -->
        <div class="col-sm-3">
          <nav id="toc" data-toggle="toc" class="sticky-top"></nav>
        </div>
        <!-- main content area -->
        <div class="col-sm-9">
        <h1>The title</h1>
          <h2>Some sub-title</h2>
          ...
          <h3>Section 1</h3>
          <h4>Subsection A</h4>
          ...
          <h4>Subsection B</h4>
          ...
          <h3>Section 2</h3>

        </div>
      </div>
    </div>
  </body>

</html>

<style>
  nav[data-toggle="toc"] {
    top: 42px;
  }

  /* small screens */
  @media (max-width: 768px) {
    /* override stickyness so that the navigation does not follow scrolling */
    nav[data-toggle="toc"] {
      margin-bottom: 42px;
      position: static;
    }

    /* PICK ONE */
    /* don't expand nested items, which pushes down the rest of the page when navigating */
    nav[data-toggle="toc"] .nav .active .nav {
      display: none;
    }

    
    /* alternatively, if you *do* want the second-level navigation to be shown (as seen on this page on mobile), use this */
    
    nav[data-toggle='toc'] .nav .nav {
      display: block;
    }
    
  }
</style>
