program annni

    implicit none

    real, dimension(2, 2) :: identity 
    complex, dimension(2, 2) :: spin_x, spin_y, spin_z
    real, allocatable, dimension(:, :) :: interaction_one, interaction_two, interaction_three
    integer :: i, j, n, m

    ! Identity

    do i = 1, 2
        do j = 1, 2
            if (i .eq. j) then
                identity(i, j) = 1
            else
                identity(i, j) = 0
            endif
        enddo
    enddo

    ! Spin X

    spin_x(1, 1) = (0, 0)
    spin_x(1, 2) = (1, 0)
    spin_x(2, 1) = (1, 0)
    spin_x(2, 2) = (0, 0)

    ! Spin Y

    spin_y(1, 1) = (0, 0)
    spin_y(1, 2) = (0, -1)
    spin_y(2, 1) = (0, 1)
    spin_y(2, 2) = (0, 0)

    ! Spin Z

    spin_z(1, 1) = (1, 0)
    spin_z(1, 2) = (0, 0)
    spin_z(2, 1) = (0, 0)
    spin_z(2, 2) = (-1, 0)

    n = 4
    m = 4

    allocate (interaction_one(n, m))
    allocate (interaction_two(n, m))
    allocate (interaction_three(n, m))

    interaction_one = 1
    interaction_two = 1
    interaction_three = 1

    ! First interaction
    
    i = 1
    do while (i .lt. n)
        do j = 1, (m - 1)
            interaction_one(i, j) = 2
            interaction_one(i, (j + 1)) = 2

            i = i + 1
        enddo
    enddo

    i = 1
    do while (i .lt. n)
        do j = 1, (m - 2)
            interaction_two(i, j) = 2
            interaction_two(i, (j + 2)) = 2

            i = i + 1
        enddo
    enddo

    i = 1
    do while (i .eq. n)
        do j = 1, m
            interaction_three(i, j) = 2
        enddo
    enddo

    do i = 1, n
        do j = 1, m
            write(*, *) interaction_one(i, j)
            write(*, *) interaction_two(i, j)
            write(*, *) interaction_three(i, j)
        enddo
    enddo

end program
