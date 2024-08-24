import React from "react";
import { Link } from 'react-router-dom'
import "./Nav.css";

const Nav = () => {
  return <nav>
    <ul>
      <li className="nav-link active"><Link to='/'>Home</Link></li>
      <li className="nav-link active"><Link to='/account'>Account</Link></li>
      <li className="nav-link "><Link to='/users-table'>Users Table</Link></li>
    </ul>
  </nav>;
};

export default Nav;
