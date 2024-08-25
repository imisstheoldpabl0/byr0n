import React, { useEffect, useState } from "react";
import axios from "axios";
import "./Account.css";

const SignupForm = () => {
  // signup form
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    login_status: false,
  });

  // login form
  const [login, setLogin] = useState({
    "username": "",
    "password": ""
  })

  // handle signup change
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // handle login change
  const handleChangeLogin = (e) => {
    const { name, value } = e.target;
    setLogin({
      ...login,
      [name]: value,
    });
  };

  // handle signup submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:8080/api/user",
        formData
      );
      console.log("Response:", response.data);
      // Handle success, maybe show a success message or redirect the user
    } catch (error) {
      console.error("There was an error!", error);
      // Handle error, maybe show an error message
    }
  };


  const deleteUsers = async () => {
    try {
      const response = await axios.delete("http://127.0.0.1:8080/api/user")
      console.error("Users deleted: " + response);
    } catch (error) {
      console.error("There was an error!", error);
    }
  }

  // handle signup login
  const handleSubmitLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.put(
        "http://127.0.0.1:8080/api/login",
        login
      );
      console.log("Response:", response.data);
      // Handle success, maybe show a success message or redirect the user
    } catch (error) {
      console.error("There was an error!", error);
      // Handle error, maybe show an error message
    }
  };

  return (
    <>
      <section id="account-section-large-all">
        <section id="larger-section">
          <form onSubmit={handleSubmitLogin} id="section-account">
            <div>
              <label>Username:</label>
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
                required
              />
            </div>
            <div>
              <label>Email:</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>
            <div>
              <label>Password:</label>
              <input
                type="password"
                name="password" sign
                value={formData.password}
                onChange={handleChange}
                required
              />
            </div>
            <button type="submit" id="sign-up-button">Sign Up</button>
          </form>
          <button type="submit" id="delete-button" onClick={deleteUsers}>Delete all users</button>
        </section>

        <section id="login-section">
          <form onSubmit={handleSubmitLogin} id="login-account">
            <div>
              <label>Username:</label>
              <input
                type="text"
                name="username"
                value={login.username}
                onChange={handleChangeLogin}
                required
              />
            </div>
            <div>
              <label>Password:</label>
              <input
                type="password"
                name="password"
                value={login.password}
                onChange={handleChangeLogin}
                required
              />
            </div>
            <button type="submit" id="log-in-button">Log In</button>
          </form>
        </section>
      </section>
    </>
  );
};

export default SignupForm;
