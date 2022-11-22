package ProjectCiclo4A.BK_seguridad.repositorios;


import ProjectCiclo4A.BK_seguridad.modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface RepositorioUsuario extends MongoRepository<Usuario, String> {
    @Query("{'correo':?0}")
    public Usuario getUserByMail(String correo);

    @Query("{'seudonimo':?0}")
    public Usuario getUserBySeudonimo(String seudonimo);
}
