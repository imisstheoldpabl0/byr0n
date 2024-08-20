import React, { useState } from "react";
import axios from 'axios'
import "./UserList.css"

const UserList = () => {

  const fetchAPI = async () => {
    const response = await axios.get("127.0.0.1.8080/api/user")
    console.log(response)
  }
  fetchAPI()

  return (
    <div id="user-list">
      <h2>This is UserData</h2>
    </div>
  );
};

export default UserList;
