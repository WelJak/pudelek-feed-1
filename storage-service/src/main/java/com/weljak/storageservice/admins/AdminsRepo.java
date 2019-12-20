package com.weljak.storageservice.admins;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AdminsRepo extends JpaRepository<Admins, String> {
    boolean existsByLoginAndPassword(String login, String password);
}
