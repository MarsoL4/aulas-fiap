using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using TDSKP.API.Infrastructure.Persistence;

namespace TDSKP.API.Infrastructure.Mappings
{
    public class UserMapping : IEntityTypeConfiguration<User>
    {
        public void Configure(EntityTypeBuilder<User> builder)
        {
            builder
                .ToTable("Users");

            builder
                .HasKey("Id");

            builder
                .Property(user => user.Name)
                .IsRequired();

            builder
                .Property(user => user.Status)
                .IsRequired();
        }
    }
}
