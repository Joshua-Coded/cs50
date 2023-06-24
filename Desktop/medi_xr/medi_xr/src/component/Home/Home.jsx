import React from "react";
import "./Home.css";

function Home() {
  return (
    <div className="header_body">
      {/* span showinglogin and support */}
      <span>
        <div>
          <img alt="img" />
          <a href="#/">
            {" "}
            <h1>Support</h1>
          </a>
        </div>
        <div>
          <img alt="img" />
          <a href="#/">
            {" "}
            <h1>Login</h1>
          </a>
        </div>
      </span>
    </div>
  );
}

export default Home;
