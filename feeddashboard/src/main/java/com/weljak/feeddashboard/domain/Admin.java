package com.weljak.feeddashboard.domain;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.Set;

@Entity
@Table(name = "admins")
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Data
public class Admin {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name="login", unique = true, nullable = false)
    public String login;

    @Column(name="password", nullable = false)
    public String password;

    @ManyToMany
    private Set<Role> roles;
}
