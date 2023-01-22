package com.project.uns.repository;
import org.springframework.data.jpa.repository.JpaRepository;
import com.project.uns.model.Professor;


public interface ProfessorRepository extends JpaRepository<Professor, Long>{

    boolean existsByJmbg(String jmbg);
    
}
