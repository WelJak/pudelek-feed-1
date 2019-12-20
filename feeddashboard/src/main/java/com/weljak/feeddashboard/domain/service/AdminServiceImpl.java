package com.weljak.feeddashboard.domain.service;

import com.weljak.feeddashboard.domain.Admin;
import com.weljak.feeddashboard.domain.repo.AdminRepository;
import com.weljak.feeddashboard.domain.repo.RoleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class AdminServiceImpl implements AdminService {
    @Autowired
    private AdminRepository userRepository;
    @Autowired
    private RoleRepository roleRepository;
    @Autowired
    private BCryptPasswordEncoder bCryptPasswordEncoder;

    @Override
    public Admin findByLogin(String login) {
        return userRepository.findByLogin(login);
    }
}
