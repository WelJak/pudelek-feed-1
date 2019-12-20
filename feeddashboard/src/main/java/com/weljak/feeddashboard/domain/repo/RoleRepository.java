package com.weljak.feeddashboard.domain.repo;

import com.weljak.feeddashboard.domain.Admin;
import org.springframework.data.jpa.repository.JpaRepository;

public interface RoleRepository extends JpaRepository<Admin, Long> {
}
