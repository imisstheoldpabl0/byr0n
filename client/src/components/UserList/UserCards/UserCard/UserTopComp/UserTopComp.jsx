import React from "react";
import "./UserTopComp.css";

const UserTopComp = () => {
  return (
    <section className="top-row">
      <table>
        <thead>
          <tr>
            <th>user_id</th>
            <th>username</th>
            <th>email</th>
            <th>password</th>
          </tr>
        </thead>
      </table>
    </section>
  );
};

export default UserTopComp;
