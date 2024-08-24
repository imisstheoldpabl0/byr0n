import React from "react";
import { Route, Routes, Navigate } from 'react-router-dom';
import Home from "./Home/Home";
import Account from "./Account/Account";
import UserList from "./UserList/UserList";
import "./MainComponent.css"

const MainComponent = () => {
  return (
    <main>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/account' element={<Account />} />
        <Route path='/users-table' element={<UserList />} />
      </Routes>
    </main>
  );
};

export default MainComponent;
