package com.weljak.feeddashboard.domain.service;

public interface SecurityService {
    String findLoggedInUsername();
    void autoLogin(String login, String password);
}
