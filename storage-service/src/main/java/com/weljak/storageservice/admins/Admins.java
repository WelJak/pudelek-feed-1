package com.weljak.storageservice.admins;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.Set;

@Entity
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "admins")
@Builder
@Data
public class Admins {
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
