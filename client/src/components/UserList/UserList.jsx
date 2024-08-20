import React, { useState, useEffect } from "react";
import axios from "axios";
import "./UserList.css";
import UserCard from "./UserCard/UserCard";

const UserList = () => {

  const [cards, setCards] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        // Petición HTTP
        const url = "http://127.0.0.1:8080/api/user"
        const response = await axios.get(url);
        let users = response.data.data;

        console.log(users)

        /*         const userObj = {
                  id_user: users.data[i][0],
                  username: users.data[i][1],
                  email: users.data[i][2],
                  password: users.data[i][3],
                  login_status: users.data[i][4],
                }; */

        console.log(userObj);
        console.log("hello");

        setCards(users
          .map((i) => i));
      } catch (e) {
        setCards([]); // No pintes nada
        console.log("CATCH");
      }
    }

    fetchData();
  }, []); // cuando hay un cambio en la ciudad se vueve a ejecutar el useEffect

  const paintCards = () => {
    return cards.length !== 0
      ? cards.map((card, index) => {
        return (
          <>
            <UserCard
              key={card.index}
              username={card.index}
              email={card.index}
              password={card[3]}
              login_status={[4]}
            />
            <p>This is UserList</p>
          </>
        );
      })
      : "";
  };

  /* const fetchAPI = async () => {
    const response = await axios.get("http://127.0.0.1:8080/api/user");
    console.log(response.data.data);
  };
  fetchAPI(); */

  return (
    <div id="user-list">

      {paintCards()}

    </div>);
};

export default UserList;
