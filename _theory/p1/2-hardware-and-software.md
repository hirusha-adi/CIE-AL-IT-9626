---
title: 2. Hardware and Software
permalink: /theory/p1/2-hardware-and-software/
layout: theory
---

## Mainframe computers and super computers

### Mainframe Computers

-   used by large organizations for bulk data processing
-   applications:
    -   censuses,
    -   statistics,
    -   transaction processing
-   Larger and more powerful than personal computers, laptops, or tablets.
-   Cost at least $75,000 in 2020.
-   Originated with large CPUs housed in steel cabinets ("main frame" or "big iron").
-   Evolved significantly despite the rise of PCs.
-   Notable feature: Reliability, Availability, and Serviceability (RAS).
-   Modern PCs have multi-core CPUs for parallel processing.
-   Mainframes have hundreds of processor cores for multitasking and multi-user operations.
-   Size has decreased from room-sized to large cupboard-sized.
-   Resistant to viruses and Trojan horses.
-   Used mainly in commercial organizations, less known to the general public.
-   example:
    -   most advanced mainframe so far is: IBM z15 (the capinet itself is taller than the average person)
    -   has 190 cores
        ![alt text](/img/notes/6.png)

#### Characteristics

-   Longevity
    -   Great longevity, can run continuously for long periods.
    -   Used by governments, banks, and telecom companies.
    -   Expensive to shut down and dispose of hardware securely.
    -   COBOL language still in use, but fewer professionals trained in it.
    -   Threats: Lack of skilled professionals, rise of Cloud computing.
    -   Solution: Combine mainframes with Cloud computing.
    -   Efficiency and dependability maintain popularity.
-   RAS (Reliability, Availability, Serviceability)
    -   Reliability: Processors self-check for errors and recover without impact.
    -   Availability: High availability with long MTBF (Mean time between failures) and quick recovery from failures.
    -   Serviceability: Can identify failure causes and replace components with minimal impact (with least/no downtime).
-   Security
    -   High level of data security, crucial for handling large volumes of personal data.
    -   Security features:
        -   Multi-factor authentication,
        -   levels of access,
        -   data encryption,
        -   secure operating systems,
        -   continual monitoring
-   Performance Metrics
    -   Speed measured in **MIPS (Millions of Instructions Per Second)**.
    -   Benchmark tests used to compare performance.
    -   Cost often linked to MIPS.
-   Volume of Input, Output, and Throughput
    -   Specialized hardware for input/output operations.
    -   Handles very large data volumes (terabytes).
    -   High throughput with billions of transactions per day.
-   Fault Tolerance
    -   Can continue operating despite component failures.
    -   Hardware and software redundancy ensures minimal disruption.
-   Operating System
    -   Can run multiple OS simultaneously **(z/OS, z/VM®, Linux®)**.
    -   Efficient parallel processing with task division among processor cores.
-   Type of Processor
    -   Hundreds of processor cores.
    -   Term 'CPU complexes' is used to describe multiple processors by some manufacturers.
-   Heat Maintenance
    -   Historically used liquid cooling, now a mix of air and water cooling.
    -   More powerful systems require effective heat management.

#### Uses

-   Banking Sector
    -   Process billions of transactions daily.
    -   Handle large volumes of data for batch processing (e.g., overnight bank statements, backups).
-   Census Data Processing
    -   Manage enormous data from population surveys.
    -   Historically used since the 1950s (e.g., UNIVAC 1).
    -   Some countries still rely on mainframes despite advances in PC processing power.
-   Industry Statistics
    -   Process data on businesses, employees, and wages.
    -   Help companies understand market trends and competitors.
-   Consumer Statistics
    -   Analyze demand for products, household incomes, and employment status.
    -   Assist in pricing, marketing, and understanding market saturation.
-   Transaction Processing
    -   Execute multiple operations to complete single transactions (e.g., bank transfers).
    -   Ensure error-free operations, maintaining data integrity.
    -   Designed for continuous availability and fault tolerance.

#### Advantages

-   High Reliability
    -   Rarely experience system downtime.
    -   Can handle hardware and software upgrades without shutting down.
-   Performance
    -   Continuously improving in speed and power.
    -   Outperform PCs, laptops, and other devices.
-   Data Handling
    -   Capable of storing and processing vast amounts of data.
    -   Can run different operating systems and handle data in various formats.
-   Security
    -   Equipped with strong encryption systems and complex authorization procedures

#### Diadvantages

-   Cost
    -   Very expensive to purchase.
    -   High costs for personnel required to run and maintain them.
-   Physical Space
    -   Require large rooms for housing.
    -   Advanced cooling systems needed, increasing installation and running costs.
-   Cloud Migration
    -   Many organizations are moving to Cloud-based services to avoid buying their own systems.
    -   Mainframe software is more expensive compared to Cloud services.

### Super Computers

-   More powerful than mainframes.
-   Can have over 100,000 processing cores.
-   Capable of massive parallel processing.
-   Example: Summit supercomputer at Oak Ridge National Laboratory (2018).
-   Summit's performance: Can perform tasks in 1 second that would take the world population 305 days.
-   Size: Fills a room the size of two tennis courts.
-   example:
    -   Cray XC40 supercomputer
        -   172 000 processor cores.
        -   Several countries have one of these for weather forecasting, scientific research, computational modelling
            ![alt text](/img/notes/7.png)

#### Characteristics

-   Longevity
    -   Short lifespan of about five years.
    -   Constantly replaced by faster models in research institutions and meteorology.
-   RAS (Reliability, Availability, Serviceability)
    -   **Not typically associated with supercomputers.**
-   Security
    -   High level of security, often with end-to-end encryption.
    -   Used for sensitive data storage like DNA profiles.
-   Performance Metrics
    -   Speed measured in **FLOPS (Floating Point Operations Per Second)**.
    -   Speeds now measured in petaflops (PFLOPS), with future targets of exaflops (EFLOPS).
-   Volume of Input, Output, and Throughput
    -   Designed for maximum processing power and speed.
    -   **Throughput is a characteristic of mainframes, not supercomputers.**
-   Fault Tolerance
    -   High likelihood of component failures due to the large number of processors.
    -   Similar fault tolerance approaches as mainframes but more prone to interruptions.
-   Operating System
    -   Typically runs **one OS, usually Linux**.
    -   Uses massively parallel processing with many processor cores, each with its own OS.
-   Type of Processor
    -   Hundreds of thousands of processor cores.
    -   Uses multiple GPUs (Graphics Processing Units).
-   Heat Maintenance
    -   Significant overheating issues due to high power consumption.
    -   Requires direct liquid cooling to manage heat.

#### Uses

-   National Defense and Data Encryption
    -   Design nuclear weapons.
    -   Encrypt sensitive data.
-   Scientific Research and Quantum Mechanics
    -   Perform calculations for atomic and subatomic particle behavior.
    -   Example: Juqueen and Juwels supercomputers in Germany.
-   Weather Forecasting
    -   Process data from weather stations, satellites, etc.
    -   Create models to predict future weather patterns.
    -   Example: UK Meteorological Office uses Cray XC40 supercomputers.
-   Climate Research
    -   Analyze long-term environmental data.
    -   Predict climate change impacts.
    -   Use models like the Community Earth System Model (CESM).
-   Drug Research
    -   Develop new medications by comparing new compounds with past research.
    -   Monitor ingredient interactions and predict drug efficacy and side effects.
-   Genetic Analysis
    -   Identify genes linked to diseases.
    -   Reduce research time from months to minutes.

#### Advantages

-   Processing Speed
    -   The fastest data processing computers available
-   Massively Parallel Processing
    -   Utilizes massively parallel processing, making them more powerful than mainframes and PCs.

#### Diadvantages

-   Cost
    -   Extremely expensive to buy and install (e.g., Summit supercomputer costs $200 million).
-   Operating Systems
    -   Typically have one operating system, unlike mainframes which can support multiple.
-   Fault Tolerance
    -   Less fault-tolerant than mainframes.
    -   More downtime compared to mainframes, though less than other systems.

### Comparison

#### Advantages vs Disadvantages of Mainframe Computers and Supercomputers

<table>
    <tr>
        <th>Category</th>
        <th>Advantages</th>
        <th>Disadvantages</th>
    </tr>
    <tr>
        <td>Mainframe Computers</td>
        <td>
            <ul>
                <li>High reliability</li>
                <li>Continuous operation during upgrades</li>
                <li>Increasing speed and power</li>
                <li>Handles vast amounts of data</li>
                <li>Runs different operating systems</li>
                <li>Strong security</li>
            </ul>
        </td>
        <td>
            <ul>
                <li>High purchase cost</li>
                <li>Expensive maintenance and personnel</li>
                <li>Requires large physical space</li>
                <li>High cooling system costs</li>
                <li>Cloud migration preferred</li>
                <li>Expensive software</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Supercomputers</td>
        <td>
            <ul>
                <li>Fastest data processing</li>
                <li>Massively parallel processing</li>
            </ul>
        </td>
        <td>
            <ul>
                <li>Extremely expensive</li>
                <li>Typically one operating system</li>
                <li>Less fault-tolerant</li>
                <li>More downtime than mainframes</li>
            </ul>
        </td>
    </tr>
</table>

#### Mainframe Computers vs. Supercomputers

<table>
    <tr>
        <th>Aspect</th>
        <th>Mainframe Computers</th>
        <th>Supercomputers</th>
    </tr>
    <tr>
        <td>Primary Use</td>
        <td>Transaction processing, batch processing, large-scale data handling</td>
        <td>Scientific research, simulations, complex calculations</td>
    </tr>
    <tr>
        <td>Speed</td>
        <td>High speed, optimized for throughput</td>
        <td>Extreme speed, optimized for parallel processing</td>
    </tr>
    <tr>
        <td>Cost</td>
        <td>Expensive to purchase and maintain</td>
        <td>Extremely expensive to purchase and install</td>
    </tr>
    <tr>
        <td>Reliability</td>
        <td>Very high reliability, minimal downtime</td>
        <td>Reliable, but less fault-tolerant than mainframes</td>
    </tr>
    <tr>
        <td>Security</td>
        <td>Strong security features, complex encryption</td>
        <td>High security, but focused more on processing power than encryption</td>
    </tr>
    <tr>
        <td>Operating Systems</td>
        <td>Supports multiple operating systems</td>
        <td>Usually runs on a single operating system</td>
    </tr>
    <tr>
        <td>Usage Examples</td>
        <td>
            <ul>
                <li>Banking transactions</li>
                <li>Census data processing</li>
                <li>Industry statistics</li>
            </ul>
        </td>
        <td>
            <ul>
                <li>Weather forecasting</li>
                <li>Climate research</li>
                <li>Drug research and simulations</li>
            </ul>
        </td>
    </tr>
</table>
