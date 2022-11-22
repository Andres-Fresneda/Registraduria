package ProjectCiclo4A.BK_seguridad.repositorios;

import ProjectCiclo4A.BK_seguridad.modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol, String> {
}
