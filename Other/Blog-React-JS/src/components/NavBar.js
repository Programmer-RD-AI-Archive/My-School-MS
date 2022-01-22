const NavBar = ({ lists }) => {
  return (
    <nav
      className="navbar_styles navbar navbar-expand-lg navbar-light bg-light"
    >
      <div style={{ marginLeft: 10 }}>
        <a class="navbar-brand" href="#">
          <img
            src="https://cdn.dribbble.com/users/2080921/screenshots/14908381/media/ead82a9b992b214980c75822f89f53dc.png?compress=1&resize=400x300"
            alt=""
            width="100"
            height="75"
            style={{ borderRadius: 125 }}
          />
        </a>
      </div>
      <div className="container-fluid">
        <a className="navbar-brand" href="#">
          Navbar
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            {lists.map((list) => (
              <li className="nav-item">
                <a className="nav-link" href={list.URL}>
                  {list["Name"]}
                </a>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
