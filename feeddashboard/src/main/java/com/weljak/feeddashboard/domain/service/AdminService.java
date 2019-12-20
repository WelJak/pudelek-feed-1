package com.weljak.feeddashboard.domain.service;

import com.weljak.feeddashboard.domain.Admin;

public interface AdminService {
    Admin findByLogin(String login);
}
